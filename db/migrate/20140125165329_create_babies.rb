class CreateBabies < ActiveRecord::Migration
  def change
    create_table :babies do |t|
      t.string :parent1
      t.string :parent2
      t.string :img1
      t.string :img2
      t.string :final

      t.timestamps
    end
  end
end
