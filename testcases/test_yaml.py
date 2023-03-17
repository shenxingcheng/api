import yaml


def test_load_yaml_file(data_dir):
    file_path = data_dir / 'goods_cat.yaml'
    with open(file_path, encoding='utf-8') as f:
        data = yaml.safe_load(f)
        assert data == {'name': 'Cactus', 'age': 18, 'skills': [['Python', 3], ['Java', 5]], 'has_blog': 'ture',
                        'gf': None}
        print(data)


def test_load_yaml_string():
    txt = """
name: Cactus
age: 18
skills:
  - - Python
    - 3
  - - Java
    - 5
has_blog: ture
gf: ~
    """
    data = yaml.safe_load(txt)
    assert data == {'name': 'Cactus', 'age': 18, 'skills': [['Python', 3], ['Java', 5]], 'has_blog': 'ture', 'gf': None}
    print(data)


# 字典转换成yaml
def test_dump_yaml_file(data_dir):
    data = {'name': 'Cactus', 'age': 18,
            'skills': [['Python', 3], ['Java', 5]],
            'has_blog': 'ture',
            'gf': None}
    txt = yaml.safe_dump(data)
    print(txt)
    with open(data_dir / 'data.yml','w')as f: # 将文件存储
        yaml.safe_dump(data,f)
