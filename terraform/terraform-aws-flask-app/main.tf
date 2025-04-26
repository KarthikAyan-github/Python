provider "aws" {
  region = "us-east-1"
}

resource "aws_security_group" "flask_sg" {
  name        = "flask-sg"
  description = "Allow HTTP and SSH"
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
    from_port   = 5000
    to_port     = 5000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "flask_instance" {
  ami           = "ami-0e449927258d45bc4"
  instance_type = "t2.micro"
  key_name      = "flask-app"

  security_groups = [aws_security_group.flask_sg.name]

  user_data = <<-EOF
    #!/bin/bash
    sudo yum update -y
    sudo yum install python3 -y
    pip install flask
  EOF

  tags = {
    Name = "FlaskAppInstance"
  }
}