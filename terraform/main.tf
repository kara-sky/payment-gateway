provider "aws" {
  region = "eu-west-1"
}

resource "aws_instance" "example" {
  count         = 1
  ami           = "ami-0c94855ba95c71c99"
  instance_type = "t2.micro"

  provisioner "remote-exec" {
    inline = [
      "sudo apt-get update",
      "sudo apt-get install -y python3-pip",
      "sudo pip3 install aiohttp",
      "nohup python3 main.py &"
    ]
  }
}
