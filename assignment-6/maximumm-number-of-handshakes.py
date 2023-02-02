#It was Raj's first day at school. His teacher Anu asked the students to meet every other student in the class and to introduce themselves. The teacher asked them to do handshakes when they meet each other.
#If there are N number of students in the class then write a program to print the total number of handshakes made by the students.
n = int(input())

handshakes = n * (n - 1) / 2
print(int(handshakes))