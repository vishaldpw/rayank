1. sudo apt-get update
2. sudo apt-get -y install podman
3. python3 --version
4. podman images
5. podman ps
6. mkdir test-podman
7. cd test-podman
8. sudo apt install python3-pip
9. python3 pip install ansible-builder/ pip install ansible-builder
10. vi execution-environment.yml
---
version: 1
build_arg_defaults:
  EE_BASE_IMAGE: quay.io/ansible/awx-ee:latest
  EE_BUILDER_IMAGE: quay.io/ansible/ansible-builder:latest
dependencies:
  #galaxy: requiredModules.yml
  python: requirements.txt
additional_build_steps:
  prepend:
    - RUN dnf upgrade -y
    - RUN pip3 install --upgrade pip setuptools

11. vi requiredModules.yml

---

collections:

  - name: ansible.utils

  - name: communnity.general

  - name: amazon.aws

12. vi requirements.txt

ansible
netmiko

14. sudo apt install python3-virtualenv
15. virtualenv -p python3.10 venv-ee-demo
16. source venv-ee-demo/bin/activate
17. pip install ansible-builder
18. ansible-builder build -t rayank_modules -v 3
19. podman create -it --name rayank-mods localhost/rayank_modules:latest
20. podman ps -a
21. podman start rayank-mods
22. podman ps -a
23. login to quay.io
24. create a repo
25. copy repo name -> quay.io/harshbaghel07/harsh
26. poddman exec -it rinki-mods bash
27. podman tag localhost/rayank_modules:latest quay.io/harshbaghel07/harsh
28. podman login quay.io
29. give username and password
30. podman container commit rinki-mods quay.io/harshbaghel07/harsh:25
31. podman image push quay.io/harshbaghel07/harsh:25
32. podman logout quay.io
33. login to ansible tower -> execution enverioment
34. name -> demo-module image->quay.io/harshbaghel07/harsh:25 

 pymsql -> image -> install using container

35. podman images
36. podman ps- a
37. podman run -it -d --name container-oin quay.io/harshbaghel07/harsh:25
38. poddman exec -it container-oin bash
39. ansible-galaxy collection list
40. pip install pymysql
41. exit
42. podman login quay.io
43. username/password
44. podman container commit container-oin quay.io/harshbaghel07/harsh:26
45. podman image push quay.io/harshbaghel07/harsh:26
46. login to tower and update the execution env with the new tag 

