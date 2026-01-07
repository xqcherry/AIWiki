from fastapi import APIRouter, Depends, HTTPException, status, Response
from typing import List

from src.services.services import DocusServices
from src.schemas.schemas import DocusCreate, DocusResponse, DocusUpdate
from src.dependency.dependency import get_docus_services


router = APIRouter(prefix="/docus", tags=["docus"])

@router.post("/", response_model=DocusResponse, status_code=status.HTTP_201_CREATED)
def create_docus(
    data: DocusCreate,
    svc: DocusServices = Depends(get_docus_services),
):
    return svc.create_document(data)

@router.get("/", response_model=List[DocusResponse])
def get_all_docus(
    skip: int = 0,
    limit: int = 100,
    svc: DocusServices = Depends(get_docus_services),
):
    return svc.get_all_document(skip, limit)

@router.get("/{document_id}", response_model=DocusResponse)
def get_docus(
    document_id: int,
    svc: DocusServices = Depends(get_docus_services),
):
    doc = svc.get_document(document_id)
    if not doc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Document not found")
    return doc

@router.put("/{document_id}", response_model=DocusResponse)
def update_docus(
    document_id: int,
    data: DocusUpdate,
    svc: DocusServices = Depends(get_docus_services),
):
    doc = svc.update_document(document_id, data)
    if not doc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Document not found")
    return doc

@router.delete("/{document_id}", response_model=DocusResponse)
def delete_docus(
    document_id: int,
    svc: DocusServices = Depends(get_docus_services),
):
    doc = svc.delete_document(document_id)
    if not doc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Document not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)





