from datetime import datetime
from typing import Dict, Any

class UserProfile:
    """
    Entidade de Negócio: Gerencia a integridade dos dados do usuário.
    Implementa validações robustas para garantir a qualidade do dado.
    """

    def __init__(self, dados: Dict[str, Any]):
        # Processamento e Validação centralizada na classe
        self.nome = self._validar_str(dados.get('nome'), "Nome")
        self.endereco = self._validar_str(dados.get('endereco'), "Endereço")
        self.sexo = self._validar_sexo(dados.get('sexo'))
        self.idade = self._validar_int(dados.get('idade'), "Idade", 0, 120)
        self.altura = self._validar_float(dados.get('altura'), "Altura", 0.5, 2.5)
        self.weight = self._validar_float(dados.get('peso'), "Peso", 2.0, 300.0)
        self.data_registro = datetime.now()

    # --- Métodos Privados de Validação ---
    def _validar_str(self, valor: str, campo: str) -> str:
        if not valor or not valor.strip():
            raise ValueError(f"❌ O campo {campo} não pode estar vazio.")
        return valor.strip().title()

    def _validar_int(self, valor: str, campo: str, min_v: int, max_v: int) -> int:
        try:
            v = int(valor)
            if not (min_v <= v <= max_v):
                raise ValueError(f"❌ {campo} deve estar entre {min_v} e {max_v}.")
            return v
        except (ValueError, TypeError):
            raise ValueError(f"❌ Entrada inválida para {campo}: '{valor}'.")

    def _validar_float(self, valor: str, campo: str, min_v: float, max_v: float) -> float:
        try:
            # Converte vírgula brasileira para ponto para evitar erros de cast
            v = float(valor.replace(',', '.'))
            if not (min_v <= v <= max_v):
                raise ValueError(f"❌ {campo} fora do intervalo realista.")
            return v
        except (ValueError, TypeError, AttributeError):
            raise ValueError(f"❌ Formato numérico inválido para {campo}: '{valor}'.")

    def _validar_sexo(self, valor: str) -> str:
        opcoes = {'M': 'Masculino', 'F': 'Feminino', 'O': 'Outro'}
        v = valor.strip().upper()
        if v not in opcoes:
            raise ValueError(f"❌ Sexo inválido. Digite M, F ou O.")
        return opcoes[v]

    def gerar_relatorio(self) -> str:
        """Separação da lógica de Saída (Output)"""
        return (
            f"\n{'='*35}\n"
            f"   📋 RELATÓRIO DO CANDIDATO\n"
            f"{'='*35}\n"
            f"👤 Nome:      {self.nome}\n"
            f"🎂 Idade:     {self.idade} anos\n"
            f"🏠 Endereço:  {self.endereco}\n"
            f"📏 Altura:    {self.altura:.2f}m\n"
            f"⚖️ Peso:      {self.weight:.1f}kg\n"
            f"🚻 Sexo:      {self.sexo}\n"
            f"📅 Registro:  {self.data_registro.strftime('%d/%m/%Y %H:%M')}\n"
            f"{'='*35}"
        )
