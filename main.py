import encrypted_dns

dns_config_object = encrypted_dns.Config()
print("Encrypted-DNS Resolver Started")
dns_server = encrypted_dns.Server(dns_config_object)
dns_server.start()