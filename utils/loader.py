from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import json
import struct
import os


FLAG_ENCRYPTED = 0x01
VERSION = 1
MAGIC = b'TBLF'


class FileLoader:
    def __init__(self, file: str):
        self._file_name = file

    def save_file(self, payload: dict):
        salt = os.urandom(16)
        nonce = os.urandom(12)
        key = derive_key(salt)

        header = {
            "file_type": "TimetableProject",
            "schema_version": 1,
            "encrypted": True,
            "kdf": "scrypt",
            "cypher": "AES-256-GCM"
        }

        header_bytes = json.dumps(header).encode("utf-8")
        payload_bytes = json.dumps(payload).encode("utf-8")

        aes_gcm = AESGCM(key)
        encrypted = aes_gcm.encrypt(nonce, payload_bytes, header_bytes)

        ciphertext = encrypted[:-16]
        tag = encrypted[-16:]

        with open(self._file_name, "wb") as f:
            f.write(MAGIC)
            f.write(struct.pack("B", VERSION))
            f.write(struct.pack("B", FLAG_ENCRYPTED))
            f.write(salt)
            f.write(nonce)
            f.write(struct.pack(">I", len(header_bytes)))
            f.write(header_bytes)
            f.write(struct.pack(">I", len(ciphertext)))
            f.write(ciphertext)
            f.write(tag)

    def load_tbl(self) -> dict:
        with open(self._file_name, "rb") as f:
            magic = f.read(4)
            if magic != MAGIC:
                raise ValueError("Invalid file type")

            version = struct.unpack("B", f.read(1))[0]
            if version != VERSION:
                raise ValueError(f"Unsupported version: {version}")

            flags = struct.unpack("B", f.read(1))[0]
            if not (flags & FLAG_ENCRYPTED):
                raise ValueError("Expected encrypted file")

            salt = f.read(16)
            nonce = f.read(12)

            header_len = struct.unpack(">I", f.read(4))[0]
            header_bytes = f.read(header_len)

            ciphertext_len = struct.unpack(">I", f.read(4))[0]
            ciphertext = f.read(ciphertext_len)
            tag = f.read(16)

        key = derive_key(salt)
        aesgcm = AESGCM(key)
        payload_bytes = aesgcm.decrypt(nonce, ciphertext + tag, header_bytes)
        return json.loads(payload_bytes.decode("utf-8"))


def derive_key(salt: bytes) -> bytes:
    kdf = Scrypt(
        salt=salt,
        length=32,
        n=2**14,
        r=8,
        p=1
    )
    return kdf.derive("90$9{|BOs~}!BZY".encode("utf-8"))
