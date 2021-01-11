<?php 

$config = [
    'database' => [
        'host' => 'localhost',
        'name' => 'images_servers',
        'user' => 'root',
        'password' => '4445552007',
    ],
    'domain' => 'aranhidImages.ru',
];
$pdo = new PDO('mysql:host=' . $config['database']['host'] . ';dbname=' . $config['database']['name'] . ';charset=utf8', $config['database']['user'], $config['database']['password']);

$uri = $_SERVER['REQUEST_URI'];

$sql = $pdo->prepare('SELECT server FROM images WHERE file=:filename');
$sql->execute([
    'filename' => substr($uri, 1),
]);

$img = $sql->fetch();

if ($img) {
    http_response_code(302);
    header('Location: ' . 'http://' . $img['server'] . '.' . $config['domain'] . $uri);
} else {
    http_response_code(404);
}