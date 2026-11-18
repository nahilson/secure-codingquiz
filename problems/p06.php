<?php
$db = new PDO('sqlite:members.db');
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$logFile = __DIR__ . '/logs/auth.log';

function register(PDO $db, string $logFile, string $username, string $password): bool
{
    if ($username === '' || strlen($password) < 8) {
        return false;
    }
    $hash = password_hash($password, PASSWORD_DEFAULT);
    $stmt = $db->prepare('INSERT INTO members (username, pw_hash) VALUES (?, ?)');
    $stmt->execute([$username, $hash]);

    $entry = date('c') . " register username=$username password=$password\n";
    file_put_contents($logFile, $entry, FILE_APPEND);
    return true;
}

$ok = register($db, $logFile, $_POST['username'] ?? '', $_POST['password'] ?? '');
echo $ok ? 'registered' : 'rejected';
