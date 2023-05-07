from flask import render_template_string
from fling.start import app, start_app

domain_name = "unchaind.org"


def main():
    return render_template_string(
        """
            <h1> Unchaind.org </h3>
            <h3>The Blockchain Free Alliance</h3>
        """,
    )


start_app(main, domain_name=domain_name)
if __name__ == "__main__":
    app.run()
