package br.com.thiago.modelo

abstract class Funcionario(
    val nome: String,
    val cpf: String,
    val salario: Double,
) {
    abstract fun getBonificacao(): Double
}