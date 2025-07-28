from fastapi import FastAPI, HTTPException
from typing import List
from models import Item
from schemas import ItemCreate, ItemUpdate

app = FastAPI(title="Inventory API")

fake_db: List[Item] = []
next_id = 1

@app.post("/items/", response_model=Item, status_code=201)
def create_item(item: ItemCreate):
    global next_id
    new = Item(id=next_id, **item.dict())
    fake_db.append(new)
    next_id += 1
    return new

@app.get("/items/", response_model=List[Item])
def list_items():
    return fake_db

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in fake_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, data: ItemUpdate):
    for idx, itm in enumerate(fake_db):
        if itm.id == item_id:
            updated = itm.copy(update=data.dict(exclude_unset=True))
            fake_db[idx] = updated
            return updated
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for idx, itm in enumerate(fake_db):
        if itm.id == item_id:
            fake_db.pop(idx)
            return {"message": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")
