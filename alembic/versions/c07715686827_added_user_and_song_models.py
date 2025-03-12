"""Added User and Song models

Revision ID: c07715686827
Revises: 5e81482f1f21
Create Date: 2025-03-12 14:11:00.770796

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c07715686827'
down_revision: Union[str, None] = '5e81482f1f21'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
