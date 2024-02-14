class User {
  String id;
  DateTime createdAt;
  String username;
  String email;
  String password;
  bool isActive;

  User({
    required this.id,
    required this.createdAt,
    required this.username,
    required this.email,
    required this.password,
    required this.isActive,
  });

  factory User.fromJson(Map<String, dynamic> json) {
    return User(
      id: json['_id']['\$oid'],
      createdAt: DateTime.parse(json['createdAt']['\$date']),
      username: json['username'],
      email: json['email'],
      password: json['password'],
      isActive: json['is_active'],
    );
  }
}
