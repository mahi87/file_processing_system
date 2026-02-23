from models.csv_upload import CSVUpload

async def save_metadata(email, blob_address, db):
    record = CSVUpload(
        user=email,
        blob_address=blob_address,
        status="uploaded"
    )
    db.add(record)
    await db.commit()
    await db.refresh(record)
    return record