<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);
?>

<!DOCTYPE html>
<html>
<head><title>Add Student</title></head>
<body>
  <h1>Add a New Student</h1>
  <form method="post">
    Name: <input type="text" name="name" required><br>
    Wants AC: <input type="checkbox" name="ac"><br>
    Wants Dining: <input type="checkbox" name="dining"><br>
    Wants Kitchen: <input type="checkbox" name="kitchen"><br>
    Wants Private Bath: <input type="checkbox" name="pb"><br>
    <button type="submit">Add Student</button>
  </form>
  <p><a href="index.html">Back to Home</a></p>

<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Escape & build args
    $name   = escapeshellarg($_POST['name']);
    $ac     = isset($_POST['ac'])     ? '1' : '0';
    $dining = isset($_POST['dining']) ? '1' : '0';
    $kitchen= isset($_POST['kitchen'])? '1' : '0';
    $pb     = isset($_POST['pb'])     ? '1' : '0';

    // Call the Python script
    $cmd = "/usr/bin/python3 add_student.py $name $ac $dining $kitchen $pb";
    exec($cmd, $output, $status);

    if ($status !== 0) {
        echo "<p style='color:red;'>Error adding student.</p>";
    } else {
        echo "<h2>Updated Student Table:</h2>";
        foreach ($output as $line) {
            echo "<pre>$line</pre>";
        }
    }
}
?>
</body>
</html>

