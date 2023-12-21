from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Susu(Base):
    __tablename__ = 'susu'
    id_susu: Mapped[str] = mapped_column(primary_key=True)
    harga: Mapped[int] = mapped_column()
    kalori: Mapped[int] = mapped_column()
    protein: Mapped[int] = mapped_column()
    lemak: Mapped[int] = mapped_column()
    ukuran: Mapped[int] = mapped_column()  
    
    def __repr__(self) -> str:
        return f"Susu(id_susu={self.id_susu!r}, harga={self.harga!r})"
