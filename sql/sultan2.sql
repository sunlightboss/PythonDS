CREATE TABLE clients (
    client_id     SERIAL PRIMARY KEY,
    first_name    VARCHAR(50) NOT NULL,
    last_name     VARCHAR(50) NOT NULL,
    birth_date    DATE NOT NULL,
    phone         VARCHAR(20) UNIQUE
);

CREATE TABLE accounts (
    account_id     SERIAL PRIMARY KEY,
    client_id      INT NOT NULL REFERENCES clients(client_id),
    account_number VARCHAR(20) UNIQUE NOT NULL,
    balance        DECIMAL(15,2) DEFAULT 0.00,
    open_date      DATE NOT NULL
);

CREATE TABLE transactions (
    transaction_id   SERIAL PRIMARY KEY,
    account_id       INT NOT NULL REFERENCES accounts(account_id),
    amount           DECIMAL(15,2) NOT NULL,
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    type             VARCHAR(10) NOT NULL
);


-- Clients (клиенты):
-- client_id: INT (PRIMARY KEY, AUTO_INCREMENT) — уникальный идентификатор; INT для целочисленного автоинкремента, эффективного хранения и индексации.
-- first_name: VARCHAR(50) — имя; VARCHAR для переменной длины строки, 50 символов достаточно для типичных имён.
-- last_name: VARCHAR(50) — фамилия; аналогично first_name.
-- birth_date: DATE — дата рождения; DATE для хранения только даты без времени.
-- phone: VARCHAR(20) — телефон; VARCHAR для форматированных номеров (с префиксами, тире).

-- Accounts (счета):
-- account_id: INT (PRIMARY KEY, AUTO_INCREMENT) — идентификатор счёта; INT для автоинкремента и индексации.
-- client_id: INT (FOREIGN KEY REFERENCES Clients(client_id)) — ссылка на клиента; INT для соответствия типу client_id.
-- account_number: VARCHAR(20) UNIQUE — номер счёта; VARCHAR для строкового формата (цифры + символы), UNIQUE для уникальности.
-- balance: DECIMAL(15,2) — баланс; DECIMAL для точных денежных значений с 2 знаками после запятой (до 13 цифр целой части).
-- open_date: DATE — дата открытия; DATE для хранения даты.

-- Transactions (операции):
-- transaction_id: INT (PRIMARY KEY, AUTO_INCREMENT) — идентификатор операции; INT для автоинкремента.
-- account_id: INT (FOREIGN KEY REFERENCES Accounts(account_id)) — ссылка на счёт; INT для соответствия типу account_id.
-- amount: DECIMAL(15,2) — сумма; DECIMAL для точных денежных значений.
--transaction_date: TIMESTAMP — дата/время операции; TIMESTAMP для хранения с точностью до секунды и временной зоны.
-- type: VARCHAR(10) — тип (deposit/withdraw); VARCHAR для коротких строковых значений.