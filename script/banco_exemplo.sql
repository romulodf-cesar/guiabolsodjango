-- 1. Criação da Tabela de Endereços (Evita redundância de dados geográficos)
CREATE DATABASE sindapp;
USE sindapp;

CREATE TABLE Endereco (
    id_endereco INT PRIMARY KEY auto_increment,
    logradouro VARCHAR(255) NOT NULL,
    cep VARCHAR(10),
    cidade VARCHAR(100),
    estado CHAR(2)
);

-- 2. Criação da Tabela de Empregados (Dados pessoais apenas)
CREATE TABLE Empregado (
    id_empregado INT PRIMARY KEY auto_increment,
    nome VARCHAR(150) NOT NULL,
    cpf VARCHAR(14) UNIQUE NOT NULL,
    identidade VARCHAR(20),
    orgao_exp_uf VARCHAR(10),
    data_nascimento DATE,
    sexo CHAR(1),
    naturalidade VARCHAR(100),
    escolaridade VARCHAR(50),
    telefone VARCHAR(20),
    id_endereco INT,
    CONSTRAINT fk_endereco_emp FOREIGN KEY (id_endereco) REFERENCES Endereco(id_endereco)
);

-- 3. Criação da Tabela de Empregadores (Entidades/Empresas)
CREATE TABLE Empregador (
    id_empregador INT PRIMARY KEY auto_increment,
    nome_entidade VARCHAR(150) NOT NULL,
    id_endereco INT,
    CONSTRAINT fk_endereco_ent FOREIGN KEY (id_endereco) REFERENCES Endereco(id_endereco)
);

-- 4. Tabela de Vínculo Trabalhista (Resolve a 2FN e 3FN)
-- Aqui ficam os dados que dependem da relação entre o empregado e a empresa
CREATE TABLE Vinculo_Trabalhista (
    id_vinculo INT PRIMARY KEY auto_increment,
    id_empregado INT NOT NULL,
    id_empregador INT NOT NULL,
    matricula VARCHAR(20) UNIQUE,
    funcao VARCHAR(100),
    lotacao VARCHAR(100),
    data_admissao DATE NOT NULL,
    CONSTRAINT fk_vinculo_empregado FOREIGN KEY (id_empregado) REFERENCES Empregado(id_empregado),
    CONSTRAINT fk_vinculo_empregador FOREIGN KEY (id_empregador) REFERENCES Empregador(id_empregador)
);