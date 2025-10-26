<?php
ini_set('display_errors',1);
ini_set('display_startup_errors',1);
error_reporting(E_ALL);

// Fetch list of students & rooms for the dropdowns
$students = [];
$rooms    = [];

// Use Python helper to fetch via SQL
exec("python3 - << 'PYCODE'
import python_db
python_db.open_database('localhost','hbraddy','eeHa9ohv','hbraddy')
print('\\n'.join([f\"{r[0]}:{r[1]}\" for r in python_db.cursor.execute('SELECT StudentId,Name FROM Student;') or python_db.cursor.fetchall()]))
python_db.close_db()
PYCODE", $students);

exec("python3 - << 'PYCODE'
import python_db
python_db.open_database('localhost','hbraddy','eeHa9ohv','hbraddy')
print('\\n'.join([f\"{r[0]}-{r[1]}\" for r in python_db.cursor.execute('SELECT BuildingId,RoomNumber FROM Room;') or python_db.cursor.fetchall()]))
python_db.close_db()
PYCODE", $rooms);
?>
<!DOCTYPE html>
<html>
<head><title>Assign Room</title></head>
<body>
  <h1>Assign Room</h1>
  <form method="post">
    Student:
    <select name="sid">
      <?php foreach($students as $s): list($id,$name)=explode(':',$s); ?>
        <option value="<?=htmlspecialchars($id)?>"><?=htmlspecialchars($name)?></option>
      <?php endforeach; ?>
    </select><br>

    Room:
    <select name="room">
      <?php foreach($rooms as $r): list($bid,$rn)=explode('-',$r); ?>
        <option value="<?=htmlspecialchars($bid.' '.$rn)?>">
          Bldg <?=htmlspecialchars($bid)?> — Room <?=htmlspecialchars($rn)?>
        </option>
      <?php endforeach; ?>
    </select><br>

    <button type="submit">Assign</button>
  </form>

  <p><a href="index.html">← Home</a></p>

<?php
if($_SERVER['REQUEST_METHOD']==='POST'){
  list($bid,$rn)=explode(' ',$_POST['room']);
  $sid = escapeshellarg($_POST['sid']);
  $bid = escapeshellarg($bid);
  $rn  = escapeshellarg($rn);

  $cmd = "python3 assign_room.py $sid $bid $rn";
  echo "<p>Running: <code>$cmd</code></p>";

  exec($cmd,$out,$st);
  foreach($out as $line) echo "<pre>$line</pre>";
}
?>
</body>
</html>
