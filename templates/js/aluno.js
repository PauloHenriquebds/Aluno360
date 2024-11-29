// Exemplo de como preencher os dados dinamicamente (se necessário)
document.addEventListener('DOMContentLoaded', function() {
    const aluno = {
        nome: "João Silva",
        turma: "8º Ano",
        serie: "8º",
        dataRelatorio: "27/11/2024",
        riscoPercentual: 85,
        riscoStatus: "Alto",
        mediaGeral: 4.2,
        notas: [3.5, 4.0, 4.8, 3.9],
        faltasTotal: 34,
        faltasPercentual: 28,
        apoioAcademico: "Sim",
        apoioPsicologico: "Não",
        reuniaoPais: "Sim",
        observacoes: "Aluno com dificuldades de concentração nas aulas e entrega irregular de tarefas."
    };

    // Preencher os dados no HTML
    document.querySelector('h1').textContent = `Relatório de Risco de Evasão Escolar - ${aluno.nome}`;
    document.querySelector('.container .section p:nth-child(2)').textContent = `Nome: ${aluno.nome}`;
    document.querySelector('.container .section p:nth-child(3)').textContent = `Turma: ${aluno.turma}`;
    document.querySelector('.container .section p:nth-child(4)').textContent = `Série: ${aluno.serie}`;
    document.querySelector('.container .section p:nth-child(5)').textContent = `Data do Relatório: ${aluno.dataRelatorio}`;

    // Risco de Evasão
    document.querySelector('.container .section:nth-child(2) p').innerHTML = `Percentual de Risco: ${aluno.riscoPercentual}% (<span class="status status-high">${aluno.riscoStatus}</span>)`;

    // Desempenho Acadêmico
    document.querySelector('.container .section:nth-child(3) p:nth-child(2)').textContent = `Média Geral: ${aluno.mediaGeral}`;
    const listaNotas = document.querySelector('.container .section:nth-child(3) ul');
    aluno.notas.forEach((nota, index) => {
        const li = document.createElement('li');
        li.innerHTML = `<strong>${index + 1}º Bimestre:</strong> ${nota}`;
        listaNotas.appendChild(li);
    });

    // Faltas
    document.querySelector('.container .section:nth-child(4) p:nth-child(1)').textContent = `Total de Faltas no Ano: ${aluno.faltasTotal}`;
    document.querySelector('.container .section:nth-child(4) p:nth-child(2)').textContent = `Percentual de Faltas: ${aluno.faltasPercentual}%`;

    // Ações Recomendadas
    document.querySelector('.actions').innerHTML = `
        <div class="action">Apoio Acadêmico: <span class="highlight">${aluno.apoioAcademico}</span></div>
        <div class="action">Apoio Psicológico: <span class="highlight">${aluno.apoioPsicologico}</span></div>
        <div class="action">Reunião com os Pais: <span class="highlight">${aluno.reuniaoPais}</span></div>
    `;

    // Observações
    document.querySelector('.container .section:nth-child(6) p').textContent = aluno.observacoes;
});
