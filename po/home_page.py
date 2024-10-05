from po.base import Base


class HomePage(Base):
    def __call__(self):
        super().__init__()
        return self.driver