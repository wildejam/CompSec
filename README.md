# Explorations in Computer Security
This repository holds 5 main projects, each located within a separate folder, and each pertaining to different subjects within Computer Security.

## 1--Crypto
The cryptography section contains 4 main parts:
- The first part involves the execution of a length-extension attack on a vulnerable md5 hash, demonstrating the importance of hashing algorithms such as SHA-256 which make use of a secret through each iteration of the block-enciphering process (see len-ext-attack.py)
- The second part involves the use of an md5 hash collision to demonstrate how scripts with the same hash can result in arbitrarily different behavior (see good.py, evil.py, prefix, and suffix. Marc Stevens' fastcoll tool is used to generate collisions)
- The third part involves creating a vigenere cipher cracker, which uses cryptanalysis techniques to determine a vigenere key given only enciphered text (see vigenere.py and populationvariance.py).
- The fourth part's attack was not implemented, but involved exploitation of the padding oracle attack on a vulnerable system.

## 2--Web
This section contains various injection strings and malicious scripts which perform various web attacks of increasing complexity. Included are various SQL injection strings, XSS scripts, XSS payloads, and CSRF bypassing scripts. Each attack iteration was developed to bypass a new defense which was introduced to counter the previous attack.

## 3--Network
This section involved utilizing the scapy library to forge packets and feign authenticity while acting as a man-in-the-middle. The first section involved intercepting network traffic between a host device and a website, and manipulating various packet fields (SYN, ACK, Flag, etc.) to create a packet which would be accepted by the host device while containing attacker-injected data. The second section involved developing a defense which would analyze a pcap capture and detect port scanners by comparing each IP address' sent SYN packets with their received SYN+ACK packets.

## 4--AppSec
Primarily concerned with the issue of buffer overflows, the Application Security section includes various vulnerable C programs and attacks which exploit their buffer overflow vulnerabilities. Each program introduces a new challenge or novel difference (DEP, Address randomization, etc.) which makes the attacks harder to execute.

## 5--AdvML
Exploring the novel concept of Adversarial Machine Learning (AdvML), this section uses rudimentary ML models developed in PyTorch and demonstrates ways of exploiting the back-propagation technique to progressively alter an image so that it will be classified incorrectly, while still looking like the same image to a human. This particular project aimed to make an arbitrary photo (cat.png) classify as Steve Wozniak to the FaceNet model.
