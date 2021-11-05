import sys

from api.models.config import Base, ENGINE, session
from api.models.devices import Device
from api.models.users import User


def main(args):
    Base.metadata.drop_all(bind=ENGINE)  # delete all tables
    Base.metadata.create_all(bind=ENGINE)  # make new tables

    device = Device("root_device")
    session.add(device)
    user = User("root")
    session.add(user)
    session.commit()


if __name__ == "__main__":
    main(sys.argv)
