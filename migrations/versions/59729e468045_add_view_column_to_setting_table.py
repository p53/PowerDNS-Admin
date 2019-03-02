"""Add view column to setting table

Revision ID: 59729e468045
Revises: 787bdba9e147
Create Date: 2018-08-17 16:17:31.058782

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "59729e468045"
down_revision = "787bdba9e147"
branch_labels = None
depends_on = None


def update_data():
    setting_table = sa.sql.table(
        "setting",
        sa.sql.column("id", sa.Integer),
        sa.sql.column("name", sa.String),
        sa.sql.column("value", sa.String),
        sa.sql.column("view", sa.String),
    )

    # just update previous records which have id <= 7
    op.execute(
        setting_table.update().where(setting_table.c.id <= 7).values({"view": "basic"})
    )

    # add more new settings
    op.bulk_insert(
        setting_table,
        [
            {"id": 8, "name": "pretty_ipv6_ptr", "value": "False", "view": "basic"},
            {"id": 9, "name": "dnssec_admins_only", "value": "False", "view": "basic"},
            {"id": 10, "name": "bg_domain_updates", "value": "False", "view": "basic"},
            {"id": 11, "name": "site_name", "value": "PowerDNS-Admin", "view": "basic"},
            {"id": 12, "name": "pdns_api_url", "value": "", "view": "pdns"},
            {"id": 13, "name": "pdns_api_key", "value": "", "view": "pdns"},
            {"id": 14, "name": "pdns_version", "value": "4.1.1", "view": "pdns"},
            {
                "id": 15,
                "name": "local_db_enabled",
                "value": "True",
                "view": "authentication",
            },
            {
                "id": 16,
                "name": "signup_enabled",
                "value": "True",
                "view": "authentication",
            },
            {
                "id": 17,
                "name": "ldap_enabled",
                "value": "False",
                "view": "authentication",
            },
            {"id": 18, "name": "ldap_type", "value": "ldap", "view": "authentication"},
            {"id": 19, "name": "ldap_uri", "value": "", "view": "authentication"},
            {"id": 20, "name": "ldap_base_dn", "value": "", "view": "authentication"},
            {
                "id": 21,
                "name": "ldap_admin_username",
                "value": "",
                "view": "authentication",
            },
            {
                "id": 22,
                "name": "ldap_admin_password",
                "value": "",
                "view": "authentication",
            },
            {
                "id": 23,
                "name": "ldap_filter_basic",
                "value": "",
                "view": "authentication",
            },
            {
                "id": 24,
                "name": "ldap_filter_username",
                "value": "",
                "view": "authentication",
            },
            {
                "id": 25,
                "name": "ldap_sg_enabled",
                "value": "False",
                "view": "authentication",
            },
            {
                "id": 26,
                "name": "ldap_admin_group",
                "value": "",
                "view": "authentication",
            },
            {
                "id": 27,
                "name": "ldap_user_group",
                "value": "",
                "view": "authentication",
            },
            {
                "id": 28,
                "name": "github_oauth_enabled",
                "value": "False",
                "view": "authentication",
            },
            {
                "id": 29,
                "name": "github_oauth_key",
                "value": "",
                "view": "authentication",
            },
            {
                "id": 30,
                "name": "github_oauth_secret",
                "value": "",
                "view": "authentication",
            },
            {
                "id": 31,
                "name": "github_oauth_scope",
                "value": "email",
                "view": "authentication",
            },
            {
                "id": 32,
                "name": "github_oauth_api_url",
                "value": "https://api.github.com/user",
                "view": "authentication",
            },
            {
                "id": 33,
                "name": "github_oauth_token_url",
                "value": "https://github.com/login/oauth/access_token",
                "view": "authentication",
            },
            {
                "id": 34,
                "name": "github_oauth_authorize_url",
                "value": "https://github.com/login/oauth/authorize",
                "view": "authentication",
            },
            {
                "id": 35,
                "name": "google_oauth_enabled",
                "value": "False",
                "view": "authentication",
            },
            {
                "id": 36,
                "name": "google_oauth_client_id",
                "value": "",
                "view": "authentication",
            },
            {
                "id": 37,
                "name": "google_oauth_client_secret",
                "value": "",
                "view": "authentication",
            },
            {
                "id": 38,
                "name": "google_token_url",
                "value": "https://accounts.google.com/o/oauth2/token",
                "view": "authentication",
            },
            {
                "id": 39,
                "name": "google_token_params",
                "value": "{'scope': 'email profile'}",
                "view": "authentication",
            },
            {
                "id": 40,
                "name": "google_authorize_url",
                "value": "https://accounts.google.com/o/oauth2/auth",
                "view": "authentication",
            },
            {
                "id": 41,
                "name": "google_base_url",
                "value": "https://www.googleapis.com/oauth2/v1/",
                "view": "authentication",
            },
        ],
    )


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("setting", sa.Column("view", sa.String(length=64), nullable=True))
    # ### end Alembic commands ###

    # update data for new schema
    update_data()


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    ## NOTE:
    ##  - Drop action does not work on sqlite3
    ##  - This action touches the `setting` table which loaded in views.py
    ##    during app initlization, so the downgrade function won't work
    ##    unless we temporary remove importing `views` from `app/__init__.py`
    op.drop_column("setting", "view")

    # delete added records in previous version
    op.execute("DELETE FROM setting WHERE id > 7")
    # ### end Alembic commands ###
