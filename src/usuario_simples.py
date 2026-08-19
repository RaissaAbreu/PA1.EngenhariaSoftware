import hashlib
from typing import List, Optional


class Usuario:
    """Representa um usuário do sistema."""

    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = self._hash_senha(senha)

    def _hash_senha(self, senha: str) -> str:
        """Gera o hash da senha."""
        return hashlib.sha256(senha.encode()).hexdigest()

    def validar_senha(self, senha: str) -> bool:
        """Verifica se a senha informada corresponde à senha cadastrada."""
        return self._hash_senha(senha) == self.senha


class GerenciadorUsuarios:
    """Gerencia os usuários necessários para o sistema atual."""

    def __init__(self):
        self.usuarios: List[Usuario] = []
        self.indice_email = {}

    def cadastrar(self, nome: str, email: str, senha: str) -> Usuario:
        """Cadastra um novo usuário, impedindo e-mails duplicados."""
        if email in self.indice_email:
            raise ValueError("Email já cadastrado")

        usuario = Usuario(nome, email, senha)
        self.usuarios.append(usuario)
        self.indice_email[email] = usuario

        return usuario

    def fazer_login(self, email: str, senha: str) -> Optional[Usuario]:
        """Realiza o login validando e-mail e senha."""
        usuario = self.indice_email.get(email)

        if usuario and usuario.validar_senha(senha):
            return usuario

        return None

    def listar_todos(self) -> List[Usuario]:
        """Retorna todos os usuários cadastrados."""
        return self.usuarios


if __name__ == "__main__":
    gerenciador = GerenciadorUsuarios()

    gerenciador.cadastrar("Ana", "ana@email.com", "123456")
    gerenciador.cadastrar("Carlos", "carlos@email.com", "abc123")

    print("Usuários cadastrados:")
    for usuario in gerenciador.listar_todos():
        print(f"- {usuario.nome} ({usuario.email})")

    usuario = gerenciador.fazer_login("ana@email.com", "123456")

    if usuario:
        print(f"Login realizado com sucesso para {usuario.nome}.")
    else:
        print("E-mail ou senha inválidos.")
