import { useState } from "react";
import { Button, Form, Input, Modal, Table } from "antd";

type Order = { id: number; name: string };
const initialOrders: Order[] = [{ id: 1, name: "Sample order" }];

export default function App() {
  const [orders, setOrders] = useState<Order[]>(initialOrders);
  const [open, setOpen] = useState(false);
  const [form] = Form.useForm<{ name: string }>();
  const submit = async () => {
    const values = await form.validateFields();
    setOrders((current) => [...current, { id: Date.now(), name: values.name }]);
    setOpen(false);
    form.resetFields();
  };
  return <main style={{ padding: 24 }}>
    <Button type="primary" onClick={() => setOpen(true)}>Create order</Button>
    <Table<Order> rowKey="id" dataSource={orders} columns={[{ title: "Order", dataIndex: "name" }]} />
    <Modal title="New order" open={open} onCancel={() => setOpen(false)} onOk={submit}>
      <Form form={form} layout="vertical"><Form.Item name="name" label="Name" rules={[{ required: true }]}>
        <Input />
      </Form.Item></Form>
    </Modal>
  </main>;
}