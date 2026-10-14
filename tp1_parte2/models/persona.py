from dataclasses import dataclass


@dataclass(frozen=True)
class Persona:
    _dni: int
    _nombre: str

    def __post_init__(self):
        if not isinstance(self._dni, int) or self._dni <= 0:
            raise ValueError("El DNI debe ser un número mayor que 0.")

        self._validar_nombre(self._nombre)

    @staticmethod
    def _validar_nombre(valor: str):
        if not isinstance(valor, str) or not valor:
            raise ValueError("El nombre no puede estar vacío.")

        if len(valor) > 30:
            raise ValueError("El nombre no puede tener más de 30 caracteres.")

        if not valor.isalpha():
            raise ValueError("El nombre solo puede contener letras.")

        if not valor[0].isupper():
            raise ValueError("El nombre debe comenzar con mayúscula.")

        if valor[1:] != valor[1:].lower():
            raise ValueError(
                "El nombre debe continuar con minúsculas."
            )

    @property
    def dni(self) -> int:
        return self._dni

    @property
    def nombre(self) -> str:
        return self._nombre
