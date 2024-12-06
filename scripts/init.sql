CREATE TABLE IF NOT EXISTS devices (
    id int PRIMARY KEY,
    model TEXT NOT NULL,
    carrier TEXT,
    firmware TEXT
);


CREATE TABLE IF NOT EXISTS clans (
    id TEXT PRIMARY KEY,
    name TEXT
);


CREATE TABLE IF NOT EXISTS inventories (
    id int PRIMARY KEY,
    cash int,
    coins int,
    item_1 int,
    item_34 int,
    item_55 int
);


CREATE TABLE IF NOT EXISTS player_profiles (
    player_id uuid PRIMARY KEY,
    credential TEXT NOT NULL,
    created timestamp with time zone,
    modified timestamp with time zone,
    last_session timestamp with time zone,
    total_spent int,
    total_refund int,
    total_transactions int,
    last_purchase timestamp with time zone,
    active_campaigns TEXT[],
    device_id int REFERENCES devices (id),
    "level" int,
    xp int,
    total_playtime int,
    country VARCHAR(2),
    language VARCHAR(2),
    birthdate DATE,
    gender TEXT,
    clan_id TEXT REFERENCES clans (id),
    inventory_id int REFERENCES inventories (id),
    _customfield TEXT

);



INSERT INTO devices (id, model, carrier, firmware) VALUES (1, 'apple iphone 11', 'vodafone', '123');
INSERT INTO inventories (id, cash, coins, item_1, item_34, item_55) VALUES (1, 123, 123, 1, 3, 2);
INSERT INTO clans (id, name) VALUES ('123456', 'Hello world clan');
INSERT INTO player_profiles (player_id, credential, created, modified, last_session, total_spent, total_refund, total_transactions,
    last_purchase, active_campaigns, device_id, "level", xp, total_playtime, country, "language", birthdate, gender,
    clan_id, inventory_id, _customfield) VALUES ('97983be2-98b7-11e7-90cf-082e5f28d836', 'apple_credential','2021-01-10 13:37:17Z','2021-01-23 13:37:17Z',
        '2021-01-23 13:37:17Z', 400, 0, 5, '2021-01-22 13:37:17Z', ARRAY[]::TEXT[], 1, 3, 1000, 144, 'CA', 'fr', '2000-01-10 13:37:17Z', 'male', '123456', 1, 'mycustom'
    );



