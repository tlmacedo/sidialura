package br.com.tlmacedo.agenda.model

class Aluno(private val nome: String, private val telefone: String, private val email: String) {
    override fun toString(): String {
        return nome
    }
}