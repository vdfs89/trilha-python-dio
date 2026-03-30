from .input_handler import input_interactive
from .user_profile import UserProfile


def main():
    try:
        dados_brutos = input_interactive()
        usuario = UserProfile(dados_brutos)
        print(usuario.gerar_relatorio())
    except ValueError as e:
        print(f"\n{e}")
    except Exception as e:
        print(f"\n⚠️ Ocorreu um erro inesperado: {e}")


if __name__ == "__main__":
    main()
