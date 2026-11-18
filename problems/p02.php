<?php
session_start();

$db = new PDO('sqlite:board.db');
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $stmt = $db->prepare('INSERT INTO comments (author, body) VALUES (?, ?)');
    $stmt->execute([$_POST['author'], $_POST['body']]);
}

$rows = $db->query('SELECT author, body FROM comments ORDER BY id DESC')->fetchAll();
?>
<!doctype html>
<html>
<body>
<h1>방명록</h1>
<ul>
<?php foreach ($rows as $row): ?>
  <li>
    <strong><?= $row['author'] ?></strong>
    <p><?= $row['body'] ?></p>
  </li>
<?php endforeach; ?>
</ul>
</body>
</html>
