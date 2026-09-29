from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(
    title="API Data Mahasiswa",
    description="Tugas 1 Integrasi Sistem",
    version="1.0.0"
)


# =========================
# MODEL DATA MAHASISWA
# =========================

class Mahasiswa(BaseModel):
    nama: Optional[str] = None
    alamat: Optional[str] = None
    ipk: Optional[float] = None
    semester: Optional[int] = None
    hobi: Optional[str] = None


# =========================
# DATABASE SEMENTARA
# =========================

mahasiswa_db = {}


# =========================
# ROOT
# =========================

@app.get("/")
def read_root():
    return {
        "message": "API Data Mahasiswa berhasil dijalankan"
    }


# =========================
# POST - TAMBAH DATA
# =========================

@app.post("/mahasiswa/{mahasiswa_id}")
async def create_mahasiswa(
    mahasiswa_id: int,
    mahasiswa: Mahasiswa
):
    if mahasiswa_id in mahasiswa_db:
        return {
            "error": "Data mahasiswa sudah ada"
        }

    mahasiswa_db[mahasiswa_id] = mahasiswa.model_dump()

    return {
        "message": "Data mahasiswa berhasil ditambahkan",
        "mahasiswa_id": mahasiswa_id,
        "mahasiswa": mahasiswa_db[mahasiswa_id]
    }


# =========================
# GET - LIHAT DATA
# =========================

@app.get("/mahasiswa/{mahasiswa_id}")
async def read_mahasiswa(mahasiswa_id: int):

    if mahasiswa_id not in mahasiswa_db:
        raise HTTPException(
            status_code=404,
            detail="Data mahasiswa tidak ditemukan"
        )

    return {
        "mahasiswa_id": mahasiswa_id,
        "mahasiswa": mahasiswa_db[mahasiswa_id]
    }


# =========================
# PUT - UPDATE DATA
# =========================

@app.put("/mahasiswa/{mahasiswa_id}")
async def update_mahasiswa(
    mahasiswa_id: int,
    mahasiswa: Mahasiswa
):

    if mahasiswa_id not in mahasiswa_db:
        raise HTTPException(
            status_code=404,
            detail="Data mahasiswa tidak ditemukan"
        )

    mahasiswa_db[mahasiswa_id] = mahasiswa.model_dump()

    return {
        "message": "Data mahasiswa berhasil diperbarui",
        "mahasiswa_id": mahasiswa_id,
        "mahasiswa": mahasiswa_db[mahasiswa_id]
    }


# =========================
# DELETE - HAPUS DATA
# =========================

@app.delete("/mahasiswa/{mahasiswa_id}")
async def delete_mahasiswa(mahasiswa_id: int):

    if mahasiswa_id not in mahasiswa_db:
        raise HTTPException(
            status_code=404,
            detail="Data mahasiswa tidak ditemukan"
        )

    deleted_mahasiswa = mahasiswa_db.pop(mahasiswa_id)

    return {
        "message": "Data mahasiswa berhasil dihapus",
        "mahasiswa_id": mahasiswa_id,
        "deleted_mahasiswa": deleted_mahasiswa
    }