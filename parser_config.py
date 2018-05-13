def parser_config():
    with open('/etc/httpd.conf') as f:
        config = {}

        lines = f.read().splitlines()
        for line in lines:
            key, value = line.split(" ")
            if key in ('cpu_limit', 'thread_limit', 'document_root'):
                config[key] = value

        return config