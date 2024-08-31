# Detailed Explanation of Internet Basics

## 1. The Internet as a Global Network
![alt text](/summer-iti-training-course/media/internet.png)
### Definition
The internet is a global system of interconnected computer networks that use standardized communication protocols to link devices worldwide. It's often described as a "network of networks".

### Brief history
- ARPANET: The precursor to the internet, developed in the late 1960s by the US Department of Defense.
- TCP/IP: Developed in the 1970s, became the standard protocol for internet communication.
- World Wide Web: Created by Tim Berners-Lee in 1989, making the internet more accessible to the public.

### Scale
As of 2024, there are over 5 billion internet users worldwide, with billions of devices connected to the internet.

## 2. Internet Service Providers (ISPs)

### Role of ISPs
ISPs are companies that provide internet access to users. They manage the infrastructure that connects individual users to the broader internet.

### Types of connections
- Broadband: Includes DSL (Digital Subscriber Line) and cable internet.
- Fiber: Uses fiber-optic cables to deliver high-speed internet.
- Cellular networks: Provide internet access to mobile devices (3G, 4G, 5G).

### ISP interaction with larger infrastructure
ISPs connect to larger networks (Tier 1 networks) that form the backbone of the internet. They also often interconnect with each other at Internet Exchange Points (IXPs).

## 3. IP Addresses

### Definition and purpose
An IP (Internet Protocol) address is a unique numerical label assigned to each device on a network. It serves two main functions:
1. Host or network interface identification
2. Location addressing

### IPv4 vs IPv6
- IPv4: Uses 32-bit addresses, allowing for about 4.3 billion unique addresses.
- IPv6: Uses 128-bit addresses, providing an vastly larger address space to accommodate the growing number of internet-connected devices.
![alt text](/summer-iti-training-course/media/image.png)
### Public vs Private IP addresses
- Public IP addresses are globally unique and used on the public internet.
- Private IP addresses are used within local networks and are not routable on the public internet.

### Dynamic vs Static IP addresses
- Dynamic IP addresses change periodically and are typically assigned by ISPs to home users.
- Static IP addresses remain constant and are often used by businesses or for hosting servers.

## 4. Data Transmission and Packets

### Packet structure
Data is divided into smaller units called packets. Each packet contains:
- Header: Information about the packet, including source and destination IP addresses.
- Payload: The actual data being transmitted.

### Benefits of packet-switching networks
- Efficient use of network resources
- Improved fault tolerance
- Ability to route around network congestion

### TCP and UDP
- TCP (Transmission Control Protocol): Provides reliable, ordered delivery of data.
- UDP (User Datagram Protocol): Offers faster, but less reliable data transmission.

### Other important protocols
- FTP (File Transfer Protocol): For transferring files
- SMTP (Simple Mail Transfer Protocol): For sending email
- POP3 and IMAP: For receiving email

## 5. Routers and Routing

### Function of routers
Routers direct data packets between different networks, determining the best path for data to travel.

### Routing tables
Routers maintain tables of network destinations and how to reach them. These tables are updated dynamically as network conditions change.

### Border Gateway Protocol (BGP)
BGP is the protocol that makes core routing decisions on the internet. It's used to exchange routing information between autonomous systems (large networks).

### Hop-by-hop routing
Data packets travel from router to router ("hop to hop") until they reach their final destination.

## 6. Domain Name System (DNS)

### Purpose of DNS
DNS translates human-readable domain names (like www.example.com) into IP addresses that computers use to identify each other.

### Hierarchical structure
DNS is organized in a hierarchical structure, with root servers at the top, followed by Top-Level Domain (TLD) servers, and then authoritative name servers for specific domains.

### Types of DNS records
- A record: Maps a domain to an IPv4 address
- AAAA record: Maps a domain to an IPv6 address
- MX record: Specifies mail servers for a domain
- CNAME record: Creates an alias from one domain to another

### DNS resolution process
1. User enters a URL in their browser
2. Browser checks its cache for the IP address
3. If not found, a request is sent to the local DNS resolver
4. The resolver queries root servers, then TLD servers, then authoritative name servers
5. The IP address is returned to the browser

## 7. Web Protocols

![alt text](/summer-iti-training-course/media/image-1.png)
### HTTP and HTTPS
- HTTP (Hypertext Transfer Protocol): The foundation of data communication on the web
- HTTPS: A secure version of HTTP that uses encryption (SSL/TLS) to protect data in transit

![alt text](/summer-iti-training-course/media/image-3.png)
### Structure of HTTP requests and responses
- Requests include method (GET, POST, etc.), headers, and sometimes a body
- Responses include a status code, headers, and usually a body


### RESTful APIs
REST (Representational State Transfer) is an architectural style for designing networked applications, commonly used for web services.

## 8. The Client-Server Model

### Explanation
In this model, clients (such as web browsers) request resources or services from servers (like web servers or database servers).

### Examples
- Clients: Web browsers, mobile apps, desktop applications
- Servers: Web servers, application servers, database servers

### Application to web browsing
When you browse a website, your browser (the client) sends requests to web servers, which respond with the requested web pages and associated resources.


### types of servers 
![alt text](/summer-iti-training-course/media/image-2.png)