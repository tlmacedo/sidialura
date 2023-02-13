package br.com.thiago.modelo

class SistemaInterno {
    fun entra(admin: Autenticavel, senha: Int) {
        if (admin.autentica(senha))
            LOG."Seja-bem vindo ao ByteBank")
        else
            LOG."houve falha na autenticação")
    }
}