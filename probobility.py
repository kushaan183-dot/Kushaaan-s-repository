total_students = 10
chess = {1, 2, 3, 4}
robotics = {3, 4, 5, 6, 7}

students_in_chess_or_robotics = chess | robotics
chance = len(students_in_chess_or_robotics) / total_students

print(f"Chance of winning: {len(students_in_chess_or_robotics)}/{total_students} = {chance:.0%}")