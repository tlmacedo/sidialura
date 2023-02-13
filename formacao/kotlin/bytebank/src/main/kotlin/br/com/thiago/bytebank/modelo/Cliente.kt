package br.com.thiago.bytebank.modelo

import br.com.thiago.bytebank.LOG
import br.com.thiago.modelo.Autenticavel

class Cliente(
    val nome: String,
    val cpf: String,
    var endereco: Endereco = Endereco(),
    private val senha: Int
) : Autenticavel {

    init {
        LOG.info("Cliente criado: ${toString()}")
    }
    override fun autentica(senha: Int): Boolean {
        return this.senha == senha
    }

    override fun toString(): String {
        return nome
    }

}