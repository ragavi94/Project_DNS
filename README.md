# Project_DNS

DNS as a Service:
Our Cloud DNS is a reliable,scalable and managed hierarchial DNS service that can be used in a Virtual Private Cloud Environment to set up Private Hosted Zones ie)DNS servers at various points in the private L2 network. The created DNS system enables the usage of private domain names for the servers/machines inside the VPC and translates the requests for the domain names into their corresponding IP addresses. 
Our DNS solution is an automated application that enables a VPC owner to  configure DNS servers as per requirement in various subnets. The application auto-generates Forward and Reverse zone files for the subnets in the DNS server and enables access of servers in the VPC through URLs in addition to their IP addresses. Our application can also configure DNS service across multiple sites that form a part of the VPC through GRE Tunneling.

System Architecture:
The system architecture contains two separate hypervisors with L2 Bridges to which Virtual Machines and namespaces are connected to.
The Virtual Machines and Namespaces act as the clients , servers and DNS servers.
GRE Tunneling is used to connect the two hypervisors to make it appear as if they exist in the same Private Network.

Feature Architecture:

1. Name Resolution within Zones
DNS server resolves the name and provides corresponding IP address configured. For example, Client 1 contacts the DNS to reach the ece server using www.ece.univ.edu. DNS resolves the address by giving the IP of any of the configured ece server. Now the client can directly reach the ece server using the obtained IP address.

2. Load Balancing of Servers
This feature balances traffic between several web servers that carry the same content/run the same application. The DNS server to which the request is made does load balancing and distributes the request by returning an IP address  from the set mapped to the same domain name in a round robin basis.

3. Location/Source IP Based Aware Resolution	
When the VPC offers a service / runs an application on a number of identically configured servers that are distributed across several subnets for redundancy / easy access purpose and the servers need to be reachable using a single domain name , but at the same time the DNS request needs to point users to the server that is closer / present in the same subnet as the client itself we use a Location Aware / Content Based Resolution.

4. High Availability / DNS Failover
When the client queries a DNS and finds that it is shutdown/ failed, then the next entry of DNS in /etc/resolv.conf file is queried for the name resolution.


