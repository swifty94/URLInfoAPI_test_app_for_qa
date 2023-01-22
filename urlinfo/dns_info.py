from dns import resolver
from dns.resolver import NoAnswer
from tld import get_tld
from base import LoggerFactory
from json import dumps
from time import sleep

class DNSInfo(object):
    def __init__(self, url: str) -> None:
        """
        - param: url | str - copy/paste any URL from browser
        - return: JSON|dict with DNS records info
        """
        self.logger = LoggerFactory.get_logger(__class__.__name__, log_level="INFO")
        self.url = url
        self.RECORDS = [
            "A",
            "AAAA",
            "NS",
            "MX",
            "TXT",
            "SOA"]
        self.logger.info("DNSInfo instance creaated")

    def get(self):
        try:
            domain = get_tld(self.url, as_object=True).fld
            self.logger.info(f"Processing: {domain}")
            result = {
                "FQDN" : domain,
                "DNS records": None
            }
            values = []
            keys = []
            count = 1
            for recordType in self.RECORDS:   
                try:      
                    get = resolver.resolve(domain, recordType)
                except NoAnswer as na:
                    values.append("NoAnwer")
                    self.logger.info(f"No record values for {recordType}")
                for record in get:
                    recId = f"{recordType}-{count}"
                    keys.append(recId)
                    values.append(record.to_text())                
                    count += 1                    
                count = 1
            dnsRecords = {}
            self.logger.info(f"Processed keys={len(keys)} values={len(values)}")
            for k in keys:
                for v in values:
                    dnsRecords[k] = v
                    values.remove(v)
                    break
            if len(dnsRecords) == 0:                
                result["DNS records"] = "No data found"
                return result
            result["DNS records"] = dnsRecords
            self.logger.info(f"Final result:\n {dumps(result, indent=4)}")
            return result        
        except Exception as e:
            self.logger.error(e, exc_info=2)