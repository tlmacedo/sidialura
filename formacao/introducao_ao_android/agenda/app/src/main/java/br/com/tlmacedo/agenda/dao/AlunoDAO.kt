package br.com.tlmacedo.agenda.dao

import br.com.tlmacedo.agenda.model.Aluno

class AlunoDAO {

    companion object {
        val alunos: MutableList<Aluno> = ArrayList()
    }

    fun salva(aluno: Aluno) {
        alunos.add(aluno)
    }

    fun todos(): MutableList<Aluno> {
        return alunos.toMutableList()
    }

}
