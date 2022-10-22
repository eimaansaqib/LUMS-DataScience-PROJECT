<?php

namespace Metacritic\API;

include './metacritic_api/metacritic.php';

if ($_SERVER['SCRIPT_FILENAME'] == __FILE__) {
    header('Content-Type: application/json');

    if (isset($_GET['game_title']) and isset($_GET['platform'])) {
        $metacritic_api = new MetacriticAPI($_GET['platform']);
        $metacritic_api->getMetacriticPage($_GET['game_title']);

        echo $metacritic_api->getMetacriticScores();
    } else {
        echo json_encode(array("error" => "Game title or platform is empty"));
    }
}

?>