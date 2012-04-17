class Meta:
    def __setattr__(self, attr, value):
        print('Setting:', attr, '=', value)
        self.__dict__[attr] = value
    
    def __getattribute__(self, attr):
        print('Getting:', attr)
        return object.__getattribute__(self, attr)

if __name__ == '__main__':
    meta = Meta()
    meta.attr = 'value'
    print('meta.attr =', meta.attr)