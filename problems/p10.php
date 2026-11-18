<?php
$db = new PDO('sqlite:clinic.db');
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

function save_patient(PDO $db, array $input): int
{
    $stmt = $db->prepare(
        'INSERT INTO patients (name, resident_no, phone) VALUES (:name, :rrn, :phone)'
    );
    $stmt->execute([
        ':name' => trim($input['name']),
        ':rrn' => $input['resident_no'],
        ':phone' => $input['phone'],
    ]);
    return (int)$db->lastInsertId();
}

function load_patient(PDO $db, int $id): array
{
    $stmt = $db->prepare('SELECT name, resident_no, phone FROM patients WHERE id = ?');
    $stmt->execute([$id]);
    return $stmt->fetch(PDO::FETCH_ASSOC);
}
