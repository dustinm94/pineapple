from investment_manager_service.investment_management_service import create_app

app = create_app()
if __name__ == "__main__":
    app.run()