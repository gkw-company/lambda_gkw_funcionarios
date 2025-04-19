CREATE TABLE test_inicializacao (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100)
);

CREATE TABLE Estabelecimento (
    estabelecimento_id VARCHAR(36) PRIMARY KEY,
    razao_social VARCHAR(255),
    cnpj VARCHAR(20),
    endereco VARCHAR(255),
    horario_funcionario VARCHAR(255)
);

CREATE TABLE Cliente (
    cliente_id VARCHAR(36) PRIMARY KEY,
    nome VARCHAR(255),
    email VARCHAR(255),
    celular DECIMAL(15,0),
    data_cadastro DATE,
    ativo BOOLEAN
);

CREATE TABLE Funcionario (
    funcionario_id VARCHAR(36) PRIMARY KEY,
    nome VARCHAR(255),
    email VARCHAR(255),
    celular VARCHAR(20),
    cpf VARCHAR(14),
    data_cadastro DATE,
    ativo BOOLEAN,
    estabelecimento_id VARCHAR(36),
    horarios_disponiveis JSON,
    FOREIGN KEY (estabelecimento_id) REFERENCES Estabelecimento(estabelecimento_id)
);

CREATE TABLE Servico (
    servico_id VARCHAR(36) PRIMARY KEY,
    descricao_servico VARCHAR(255)
);

CREATE TABLE situacao_agendamento (
    situacao_id VARCHAR(36) PRIMARY KEY,
    descricao_situacao VARCHAR(255)
);

CREATE TABLE Agendamento (
    agendamento_id VARCHAR(36) PRIMARY KEY,
    cliente_id VARCHAR(36),
    funcionario_id VARCHAR(36),
    estabelecimento_id VARCHAR(36),
    data_hora DATE,
    servico_id VARCHAR(36),
    situacao_id VARCHAR(36),
    FOREIGN KEY (cliente_id) REFERENCES Cliente(cliente_id),
    FOREIGN KEY (funcionario_id) REFERENCES Funcionario(funcionario_id),
    FOREIGN KEY (estabelecimento_id) REFERENCES Estabelecimento(estabelecimento_id),
    FOREIGN KEY (servico_id) REFERENCES Servico(servico_id),
    FOREIGN KEY (situacao_id) REFERENCES situacao_agendamento(situacao_id)
);
