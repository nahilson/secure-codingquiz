<?php
session_start();

if (!isset($_SESSION['user_id'])) {
    http_response_code(401);
    exit;
}

$db = new PDO('sqlite:bank.db');
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

$to = $_POST['to_account'] ?? '';
$amount = (int)($_POST['amount'] ?? 0);

if ($to !== '' && $amount > 0) {
    $db->beginTransaction();
    $debit = $db->prepare('UPDATE accounts SET balance = balance - ? WHERE user_id = ?');
    $debit->execute([$amount, $_SESSION['user_id']]);
    $credit = $db->prepare('UPDATE accounts SET balance = balance + ? WHERE number = ?');
    $credit->execute([$amount, $to]);
    $db->commit();
    echo 'transfer done';
}
