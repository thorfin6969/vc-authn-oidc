"""auth_session_table

Revision ID: 65eab74c2e3c
Revises: 1330a916991a
Create Date: 2023-01-05 20:50:08.828204

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel

from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "65eab74c2e3c"
down_revision = "1330a916991a"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "auth_sess_auth_sessions",
        sa.Column(
            "presentation_exchange",
            postgresql.JSON(astext_type=sa.Text()),
            nullable=True,
        ),
        sa.Column(
            "request_parameters", postgresql.JSON(astext_type=sa.Text()), nullable=True
        ),
        sa.Column(
            "uuid",
            sqlmodel.sql.sqltypes.GUID(),
            server_default=sa.text("gen_random_uuid()"),
            nullable=False,
        ),
        sa.Column("expired_timestamp", sa.DateTime(), nullable=False),
        sa.Column("ver_config_id", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("pres_exch_id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("verified", sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint("uuid"),
    )
    op.create_index(
        op.f("ix_auth_sess_auth_sessions_uuid"),
        "auth_sess_auth_sessions",
        ["uuid"],
        unique=True,
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(
        op.f("ix_auth_sess_auth_sessions_uuid"), table_name="auth_sess_auth_sessions"
    )
    op.drop_table("auth_sess_auth_sessions")
    # ### end Alembic commands ###