from problem_solving.crm.CustomerManagement import CustomerManagement
from SalesTracking import SalesTracking
from Reporting import Reporting

if __name__ == "__main__":
    customer_mgmt = CustomerManagement()
    sales_mgmt = SalesTracking()
    report_mgmt = Reporting(customer_mgmt, sales_mgmt)

    # Adding Customers
    print(customer_mgmt.add_customer("Alice Johnson", "alice@example.com", "123-456-7890"))
    print(customer_mgmt.add_customer("Bob Smith", "bob@example.com", "987-654-3210"))

    # Recording Sales
    print(sales_mgmt.record_sale("Alice Johnson", "Laptop", 1200))
    print(sales_mgmt.record_sale("Bob Smith", "Smartphone", 800))

    # Generating Report
    print(report_mgmt.generate_report())