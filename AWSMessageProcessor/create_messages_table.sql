CREATE TABLE messages (
    id INT PRIMARY KEY,            -- Identificador único
    name NVARCHAR(100) NOT NULL,   -- Nombre asociado al mensaje
    value DECIMAL(10, 2) NOT NULL, -- Valor del registro
    timestamp DATETIME NOT NULL    -- Fecha y hora del mensaje
);
